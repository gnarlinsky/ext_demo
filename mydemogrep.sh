# print filenames; don't ignore case, 4 line of context; line number; recursive;
# exclude certain directories... like -- don't search through all of Django's code, obv
grep --ignore-case --color --line-number --recursive --context=4 --exclude-dir={archive,htmlcov,.git,ve_django15} --exclude={*.db,*.pyc,*.swp}  "$1" "$2"; 
#grep --color --line-number --recursive --context=4 --exclude-dir={archive,htmlcov,.git} --exclude={*.db,*.pyc,*.swp} "$1" "$2"; 
echo ""
echo "#############################################"
echo "# Summary:"
echo "#############################################"
grep --ignore-case --recursive --files-with-matches --exclude-dir={htmlcov,archive,.git,ve_django15} --exclude={*.db,*.pyc,*.swp} "$1"  "$2"; 
#grep --recursive --files-with-matches --exclude-dir={htmlcov,archive,.git} --exclude={*.db,*.pyc,*.swp} "$1"  "$2"; 

