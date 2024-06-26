import yaml
from pathlib import Path
from logging.config import dictConfig


def get_filename_in_dir(dir: Path) -> str | None:
    """Returns FIRST filename from the list of files found in given directory

    Document versions are stored in following format:
    ```
        /<media-root>/<prefix>/ab/cd/abcd12c...a/<file-name>.<ext>

    Where abcd12c...a is the UUID of the document version.
    This method returns the <file-name>.<ext> part - which is assumed
    to be the only file in the directory.
    ```
    """
    results = dir.glob('*', case_sensitive=False)
    for item in results:
        # it is the only file in the directory
        return item.name

    return None


def setup_logging(config: Path):
    if config is None:
        return

    with open(config, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)

    dictConfig(config)
