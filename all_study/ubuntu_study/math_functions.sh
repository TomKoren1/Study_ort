add(){
	sum=0
	for arg in "$@"; do
		sum=$((sum+arg))
	done
	echo $sum
}

sub(){
	sum=$1
	for num in "${@:2}"; do
		sum=$((sum-num))
	done
	echo $sum
}

mult(){
	sum=$1
	for num in "${@:2}"; do
		sum=$((sum*num))
	done
	echo $sum
}

pow(){
	sum=$1
	for((i=1;i<$2;i++)); do
		sum=$((sum*$1))
	done
	echo $sum

}

devide(){
	sum=$1
	for num in "${@:2}"; do
		sum=$((sum/num))
	done
	echo $sum
}

even(){
	if (($1%2==0)); then
		echo "the number $1 is even"
	else
		echo "the number $1 is not even"
	fi
}
