from shared.utils import CONTENT_FOLDER_PREFIX, FOOTER


def main(argv=None):
    print(f"""
############################################################
First read these instructions. Then do it!

You will only need one (1) web-bash terminal for this example.

1. First, open a new browser window. Go to:

     https://www.hadabot.com/tools/teleop.html

2. In this web-bash terminal, type the following, ** one line at a time **:

     source /opt/ros/eloquent/setup.bash

     ros2 topic echo /base_controller/command

3. Switch back to the "ROS2 - Teleop" browser window.

   a. It should say "Status: Connected to your local ROS2...".

   b. Click the arrow buttons and you should see messages displayed in the web-bash terminal screen that's running "ros2 topic echo..."

{FOOTER}
############################################################
""")


if __name__ == "__main__":
    main()
