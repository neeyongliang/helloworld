#!/bin/zsh
#maybe you are using bash,fix the first line.
#!/bin/zsh
# Program:
#	calculate
#History:
#2015/xx/xx  wikinee First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin/:~/bin
export PATH

echo -e "You SHOULD input 2 numbers,i will cross them! \n"
read -p "first number:" firstnu
read -p "last number:" secnu

total=$(($firstnu*$secnu))

echo -e "\nThe result os $firstnu x $secnu is ==> $total"

