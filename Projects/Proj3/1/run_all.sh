#!/bin/bash

OUTPUT_FILE="results.txt"

# Clear the output file
truncate -s 0 $OUTPUT_FILE

# Array of instance files (adjust paths as needed)
INSTANCES=(
    "rlfap/var2-f24.txt rlfap/dom2-f24.txt rlfap/ctr2-f24.txt"
    "rlfap/var2-f25.txt rlfap/dom2-f25.txt rlfap/ctr2-f25.txt"
    "rlfap/var3-f10.txt rlfap/dom3-f10.txt rlfap/ctr3-f10.txt"
    "rlfap/var3-f11.txt rlfap/dom3-f11.txt rlfap/ctr3-f11.txt"
    "rlfap/var6-w2.txt rlfap/dom6-w2.txt rlfap/ctr6-w2.txt"
    "rlfap/var7-w1-f4.txt rlfap/dom7-w1-f4.txt rlfap/ctr7-w1-f4.txt"
    "rlfap/var7-w1-f5.txt rlfap/dom7-w1-f5.txt rlfap/ctr7-w1-f5.txt"
    "rlfap/var8-f10.txt rlfap/dom8-f10.txt rlfap/ctr8-f10.txt"
    "rlfap/var8-f11.txt rlfap/dom8-f11.txt rlfap/ctr8-f11.txt"
    "rlfap/var11.txt rlfap/dom11.txt rlfap/ctr11.txt"
    "rlfap/var14-f27.txt rlfap/dom14-f27.txt rlfap/ctr14-f27.txt"
    "rlfap/var14-f28.txt rlfap/dom14-f28.txt rlfap/ctr14-f28.txt"
)

# Array of algorithms
ALGORITHMS=("fc-cbj")

# write to both terminal and file
echo "" | tee -a $OUTPUT_FILE

# Loop through each instance
for instance in "${INSTANCES[@]}"; do
    # Split instance into var, dom, ctr files
    read -r VAR DOM CTR <<< "$instance"
    
    echo "======================================" | tee -a $OUTPUT_FILE
    echo "Instance: $VAR" | tee -a $OUTPUT_FILE
    echo "======================================" | tee -a $OUTPUT_FILE
    echo "" | tee -a $OUTPUT_FILE
    
    # Loop through each algorithm
    for algo in "${ALGORITHMS[@]}"; do
        echo "Running $algo on $VAR..." | tee -a $OUTPUT_FILE
        echo "-----------------------------------" | tee -a $OUTPUT_FILE
        
        # Run the algorithm and append output to file
        python3 rlfa.py "$VAR" "$DOM" "$CTR" "$algo" 2>&1 | tee -a $OUTPUT_FILE
        
        echo "" | tee -a $OUTPUT_FILE
        echo "-----------------------------------" | tee -a $OUTPUT_FILE
        echo "" | tee -a $OUTPUT_FILE
    done
    
    echo "" | tee -a $OUTPUT_FILE
done

echo "All experiments completed!" | tee -a $OUTPUT_FILE
