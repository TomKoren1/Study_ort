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
