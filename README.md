# Fetch Coding Exercise

**Problem:** Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar, but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake gold bar by only bars and balance scales. You can only place gold bars on scale plates (bowls) and find which scale weighs more or less.

**Solutions**

**Note:** As time is a constraint, we will hardfit the solution for 9 bars. The solution can be generalized for n bars using the same approach.

1. **Brute Force:** Compare each bar with each other till we find the lighter bar.
2. **Divide and Conquer:** 
    1. Divide the bars into 3 groups of 3 bars each. 
    2. Weigh two groups.
    3. If they are equal, the fake bar is in the third group.
    4. If they are not equal, the fake bar is in the lighter group.
    5. Repeat the process with the lighter group. 
    6. Continue until you find the fake bar.

We will implement the second solution as it is more efficient.

**Implementation**: 
1. We will implement the solution in Python.
2. Selenium WebDriver will be used to automate the browser.
**Note:** We have added a delay of 2 seconds in multiple places to make the process visible. This can be removed to make the process faster when implemented as part of an automated system.

**Steps to run the code:**
1. Install Python 3.8 or higher from https://www.python.org/downloads/.
2. Install Latest version of Chrome Browser from https://www.google.com/chrome/.
3. Clone this repository using the command `git clone https://github.com/mshasan2/Fetch_Rewards.git`.
4. Install the required libraries using the command `pip install -r requirements.txt`.
5. Navigate to the directory where the code is cloned.
6. Run the command `python findFakeBar.py` in terminal / command prompt. The result will be displayed in the terminal.

**Execution Video Link** https://www.youtube.com/watch?v=jToJl3swLwA