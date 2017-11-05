if [ ! -z "$1" ]; then
	sortmethod=$1
	echo "Setting sorting method to ${sortmethod}"
fi

for size in 10 100 500 1000 5000 10000; do
	if [ -z "${sortmethod}" ]; then
		time=`python3 -m cProfile challenge_5.py inputs_for_timing/input_${size}.txt output.txt | grep "function calls" | awk '{print $8}'`
	else
		time=`python3 -m cProfile challenge_5.py inputs_for_timing/input_${size}.txt output.txt -a ${sortmethod} | grep "function calls" | awk '{print $8}'`
	fi
	echo "${size},${time}"
done
