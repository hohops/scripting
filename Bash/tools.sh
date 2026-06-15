#!/bin/bash

On_IGreen='\033[0;102m'
UNDERLINE='\033[4m'
NC='\033[0m'
BLINK_WHITE="\033[5;97m"
echo ""
echo ""
cat <<'EOF' | sed 's/./\x1b[94m&\x1b[0m/g'

        				 /$$      /$$           /$$
                        	       	| $$  /$ | $$          | $$
                       	        	| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$
                     	          	| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
                       	        	| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
                        	       	| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
                       	        	| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$
                       	        	|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/

EOF
echo ""
echo -e "								 ${UNDERLINE}Press 1 to start!${NC}"
echo ""
echo ""
echo -e "${UNDERLINE}${BLINK_WHITE}Press 1${NC}"
read pressed1

while [ "$pressed1" != "1" ]; do
    echo -e "${UNDERLINE}${BLINK_WHITE}Press 1${NC}"
    read -r -n1 pressed1
    echo  # This moves to a new line after the keypress
done

echo '								Welcome to the tool workshop!'
sleep 1
echo -e "								Chose ${UNDERLINE}1${NC} tool"
sleep 0.5
echo "								1 - addiction calculator"
echo "								2 - Go to a computer section"


echo
echo -e "${UNDERLINE}${BLINK_WHITE}Chose one tool${NC}"
read option
if [ "$option" = "1" ]; then
	echo "Enter first number:"
	read a
	echo "Enter second number:"
	read b
	echo "Sum: $((a + b))"
fi
if [ "$option" = "2" ]; then
	echo "								Where would you like to go?"
	sleep 0.5
	echo "	  							   	1 - Downloads"
	echo "	  							   	2 - Desktop"
	echo "	  							        3 - Documents"
	echo "	  							        4 - Videos"
	echo "  									5 - Images"
	echo " Chose where to go:"
read folderN

fi

if [ "$folderN" = "1" ]; then
	cd Downloads
	echo "You are now in Downloads"
fi

if [ "$folderN" = "2" ]; then
	cd Desktop
	echo "You are now in the Desktop"
fi
if [ "$folderN" = "3" ]; then
	cd Documents
	echo "You are now in documents"
fi
