This project requires the following dependencies:
- Python 3.8, 3.9, 3.10 or 3.11 (e.g. installed via WinPython [dot version])
- Dependencies listed in `requirements.txt` (e.g. installed via `pip install -r requirements.txt`)

Context:
- This project is a simplified version of a real project
- The goal is to find the best translation between two sets of disks which
  represent ball positions in 2D space. One set is the theoretical positions
  and the other set is the measured positions. The theoretical positions are
  computed with an algorithm which is not perfect, so that we know that there
  is a translation error between the two sets of disks. The goal is to find
  the translation which minimizes the error.

Note:
The solution may of course rely on additionnal dependencies.

Goal:
- Write the missing code in `bestfit_unit.py` to make the unit test pass:
  the code should be a function named `best_fit_translation` and located
  in a missing module named `processing.py`
- Run `python bestfit_unit.py` to run the test which helps you to check your code

Further information:
- Please read the docstrings in `bestfit_unit.py`