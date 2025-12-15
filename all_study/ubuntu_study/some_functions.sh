make_copy(){
	dir_to_backup=$1
	results=$(find $HOME -d -name $dir_to_backup 2> /dev/null)
	choise=""
	select r in $results;do
		choice=$r
		break
	done
	backup_name=$(basename $choice 2> /dev/null)-$(date "+%d-%m-%Y")
	dir_path=${choice%/*}
	full_path="$dir_path/$backup_name"
	results_backup_name=$(find $full_path 2> /dev/null)
	if [ -n "$results_backup_name" ]; then
		read -p "already backed up today, want to overide?" ans
		if [ "$ans" = "no" ];then
			echo "nope"
		else
			echo "overiding"
			tar -czf "$full_path" "$choice"
		fi
	else
		echo "creating new backup"
		tar -czf "$full_path" "$choice"
	fi
}

lsdirs(){
	allfiles=$(ls -d */)	
	echo "$allfiles"
}
see(){
	if [ -d $1 ]; then
		echo $(ls $1)
	else
		echo $(more $1)
	fi
}
how_long(){
	word=$1
	echo "the word $word is ${#word} characters long"
}

biggest_number(){
	num1=$1
	num2=$2
	num3=$3
	if [[ ! $num1 =~ ^-?[0-9]+$ || ! $num2 =~ ^-?[0-9]+$ || ! $num3 =~ ^-?[0-9]+$ ]]; then
		echo "error invalid input"
		return 1
	fi
	if [ $num1 -gt $num2 -a $num1 -gt $num3 ]; then
		echo "$num1 is the biggest"
	fi
	if [ $num2 -gt $num1 -a $num2 -gt $num3 ]; then
		echo "$num2 is the biggest"
	fi
	if [ $num3 -gt $num1 -a $num3 -gt $num2 ]; then
		echo "$num3 is the biggest"
	fi
}

simple_calc(){
	num1=$1
	num2=$3
	sign=$2
	if [[ ! $num1 =~ ^-?[0-9]+$ || ! $num2 =~ ^-?[0-9]+$ ]]; then
                echo "error invalid numbers input"
                return 1
	fi
	case "$sign" in 
		"+")
			echo "$((num1 + num2))"
			;;
		"-")
			echo "$((num1 - num2))"
			;;
		"X")
			echo "$((num1 * num2))"
			;;
		"/")
			echo "$((num1 / num2))"
			;;
		*)
			echo "invalid sign"
			;;

	esac
}

rev_number(){
	if [[ ! $1 =~ ^-?[0-9]+$ ]]; then
		echo "not a number"
		return 1
	fi
	echo $(echo $1 | rev)
}

sum_of_digits(){
	num=$1
	sum=0
	while [ $num -gt 0 ]
	do
		sum=$((sum+num%10))
		num=$((num/10))
	done
	echo "$sum"
}

findLine(){
	startLine=$1
	countLines=$2
	file_cut=$(cat $3)
	for (( i=$startLine; i<(($startLine+$countLines)); i++))
	do
		echo "$i"
	done

}
