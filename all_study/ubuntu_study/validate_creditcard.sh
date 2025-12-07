multiply_digits(){
rev_card_num=$1
rev_card_num=${rev_card_num:1}
new_nums=""
flag="0"
let sum=0
for digit in $(echo "$rev_card_num" | grep -o .); do
	let num=$digit
	if [ $flag -eq "1" ]; then
                flag="0"
        else
		num=$((num*2))
                flag="1"
        fi
	if [ $num -ge 10 -a $flag -eq "1" ]; then
		num=$((num%10+num/10))
	fi
	sum=$((sum+num))
	new_nums="${new_nums}${num}"
done
echo "$sum"
}
card_company(){
digit=$1
if [ $digit -eq "3" ]; then
	echo "Diners club or American Express"
elif [ $digit -eq "4" ]; then
	echo "Visa"
elif [ $digit -eq "5" ]; then
	echo "MasterCard"
elif [ $digit -eq "6" ]; then
	echo "Discover"
fi
}

validate_card(){
card_num=$1
let check_digit="${card_num: -1}"
first_digit="${card_num:0:1}"
sum_of_multi=$(multiply_digits $(echo $card_num | rev))
check=$((sum_of_multi+check_digit))
if [ $((check % 10)) -eq 0 ]; then
	echo "correct"
else
	echo "incorrect card"
fi
card_company $first_digit
}


