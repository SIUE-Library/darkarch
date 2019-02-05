cut -c2- output.txt | sort > temp.txt; python2 identify_dup.py temp.txt;
