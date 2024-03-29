import glob
import os
from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Dict, List, Optional, Union

import geopandas as gpd
import pandas as pd


class SDGBase(ABC):
    """Defines input and output directories for data, use of relevant read methods for data
    and joining of pandas and geopandas dataframes.

    Attributes
    ----------
    root_dir
        The main directory in which data is stored.
    input_data_dir
        The main directory from which data is input.
    output_data_dir
        The main directory to which data is output.
    test_in_dir
        The main directory from which tests are drawn.
    test_out_dir
        The main directory to which tests are output.
    """

    def __init__(
        self,
        sdg_name: str,
        root_dir: Optional[str],
        data_dir: Optional[str] = None,
        output_dir: Optional[str] = None,
        logger: bool = False,
    ) -> None:
        """Defines input and output directories for data.

        Parameters
        ----------
        root_in_dir: str
            The main directory in which data is stored.
        root_out_dir: Optional[str]
            This is for if the user wants to save the output elsewhere.
            If not the root out directory will be the same as the input directory.

        Returns
        -------
        None
        """

        self._root_dir: Optional[str] = root_dir
        self._sdg_name: str = sdg_name
        self._logger: bool = logger

        self.set_file_tree(data_dir, output_dir)

    def set_input_data_dir(self, root_in_dir: Optional[str]) -> None:
        """Sets directory and creates folders from which data is input.

        Parameters
        ----------
        root_in_dir: str
            The main directory in which data is stored.

        Returns
        -------
        None
        """

        self._input_data_dir: Optional[str] = root_in_dir
        self.create_folders(self._input_data_dir)

    def get_input_data_dir(self) -> Optional[str]:
        """returns main directory in which data is stored.

        Returns
        -------
        str
        """
        return self._input_data_dir

    def set_output_data_dir(self, root_out_dir: Optional[str]) -> None:
        """sets directory and creates folders for data outputs.

        Parameters
        ----------
        root_out_dir: str
            The directory in which outputs are stored.

        Returns
        -------
        None
        """

        self._output_data_dir: Optional[str] = root_out_dir
        self.create_folders(self._output_data_dir)

    def get_output_data_dir(self) -> Optional[str]:
        """Returns directory in which outputs are stored.

        Returns
        -------
        str
        """

        return self._output_data_dir

    def set_file_tree(
        self,
        input_data_dir: Optional[str] = None,
        output_data_dir: Optional[str] = None,
    ) -> None:
        """Sets file tree for input and output data.

        Parameters
        ----------
        input_data_dir: str
            The main directory from which data is input.
        output_data_dir
            The main directory to which data is output.

        Returns
        -------
        None
        """

        if input_data_dir is None:
            self._input_data_dir = f"{self._root_dir}/{self._sdg_name}_data"
        else:
            self._input_data_dir = input_data_dir

        if output_data_dir is None:
            self._output_data_dir = f"{self._root_dir}/{self._sdg_name}_output"
        else:
            self._output_data_dir = output_data_dir

        self._test_in_dir: str = f"{self._root_dir}/tests_data/{self._sdg_name}_data"
        self._test_out_dir: str = f"{self._root_dir}/tests_data/{self._sdg_name}_output"

        file_tree: List[str] = [
            self._input_data_dir,
            self._output_data_dir,
            self._test_in_dir,
            self._test_out_dir,
        ]

        for branch in file_tree:
            self.create_folders(branch)

    def create_folders(self, new_dir: str) -> None:
        """Creates folders to store output data.

        Parameters
        ----------
        new_dir: str
            Directory in which to store output data.

        Returns
        -------
        None

        Raises
        -------
            Catches any error in making the file.
        """

        try:
            os.makedirs(new_dir, exist_ok=True)
            if self._logger:
                print(f"Directory {new_dir} was created or already existed")
        except Exception as e:
            print(f"Unable to make directory {new_dir} because of error {e}")

    def get_ext_files(
        self, inp_folder: str, ext: str, search_string: Optional[str] = None
    ) -> List[str]:
        """Retrieves input files by extension with optional file name filtering.

        Parameters
        ----------
        inp_folder: str
            Folder containing input data of interest.
        ext: str
            Files must have this extension
        search_string: Optional[str]
            File names must contain this string

        Returns
        -------
        list[str]
        """
        all_files: List[str] = glob.glob(
            f"{self.get_input_data_dir()}/{inp_folder}/*.{ext}"
        )
        if search_string:
            all_files = [f for f in all_files if search_string in f]
        return all_files

    def _get_read_function(self, ext: str) -> Callable:
        """Returns the relevent read method based on the
           input extension.

        Parameters
        ----------
        ext: str
            The extension being searched for

        Returns
        -------
        Callable
        """
        data_read_dict = {
            "csv": pd.read_csv,
            "shp": gpd.read_file,
            "gpkg": gpd.read_file,
            "xls": pd.read_excel,
            "xlsx": pd.read_excel,
        }
        return data_read_dict[ext]

    def load_data(
        self,
        file_path: str,
        cols: Optional[List[str]] = None,
        index: Optional[str] = None,
        epsg: int = 27700,
        kwargs: Optional[Dict[str, str]] = None,
    ) -> Union[pd.DataFrame, gpd.GeoDataFrame]:
        """Joins and loads data as a data frame.

        Parameters
        ----------
        file_path: str
            Location of files of interest.
        cols: List[str]
            Only return columns in this list.
        index: str
            Set index to this column
        espg: int
            ESPG code of coordinate reference system used in files of interest.
        kwargs: Dict[str, str]
            Key word arguments for the read method
        Returns
        -------
        File: Union[pd.DataFrame, gpd.GeoDataFrame]
        """
        if not kwargs:
            kwargs = {}
        ext: str = file_path.split(".")[-1]
        read_func = self._get_read_function(ext)
        df: Union[pd.DataFrame, gpd.GeoDataFrame] = read_func(file_path, **kwargs)
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.strip()
        if cols:
            df = df[cols]
        if index:
            df = df.set_index(index)
        if isinstance(df, gpd.GeoDataFrame) and not df.crs.to_epsg() == epsg:
            df = df.to_crs(epsg)
            df = df.set_geometry(df["geometry"])

        return df

    def save_data(
        self, file: Union[pd.DataFrame, gpd.GeoDataFrame], file_name: str
    ) -> bool:
        """Saves data as .csv or .shp, dependent on dataframe.

        Parameters
        ----------
        file: Union[pd.DataFrame, gpd.DataFrame]
            Data to save
        file_name: str
            Name for saved file.

        Returns
        -------
        bool
        """
        if isinstance(file, pd.DataFrame):
            file.to_csv(f"{self.get_output_data_dir()}/{file_name}.csv")
        if isinstance(file, gpd.GeoDataFrame):
            file.to_file(f"{self.get_output_data_dir()}/{file_name}.shp")
        return True

    @abstractmethod
    def calculate_sdg(self) -> None:
        pass
