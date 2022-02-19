from shutil import rmtree
import subprocess
import sys
import tempfile
import venv


def main():
    tmp_venv = tempfile.mkdtemp()
    venv.create(tmp_venv, with_pip=True)
    subprocess.run([f"{tmp_venv}/bin/pip", "install", "pyfiglet"])

    if len(sys.argv) == 2:
        subprocess.run([f"{tmp_venv}/bin/python3", "-m", "figdate", sys.argv[1]])
    elif len(sys.argv) == 3:
        subprocess.run(
            [f"{tmp_venv}/bin/python3", "-m", "figdate", sys.argv[1], sys.argv[2]]
        )
    else:
        subprocess.run([f"{tmp_venv}/bin/python3", "-m", "figdate"])
    rmtree(tmp_venv)


if __name__ == "__main__":
    main()
