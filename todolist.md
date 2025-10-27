# Reviews
* A.1: Speculative pass is consuming much compute resource without API instrumented, which is more than the benefits
* A.2: Experiments are running under small scale and restriction is artificially low
* B.1: Workload may be non-deterministic under multithread situation with dynamic partitioned workload
* C.1: Manual annotation is required and is error prone
* C.2: Some words in paper could be simplified
* C.3: Having some numbers of (data size / program) to motivate design
* C.4: Why not a standard design of memory allocator that separates metadata from data (e.g., Hoard, slab) work?
* C.5: Could the data sizes for the program be provided at compile time to create a more efficient heap?
* C.6: Layout the requirements of speculative pass to better justify the design choice
* C.7: Explain how MERLIN_TOUCH references are ordered with respect to page faults as the faults are passed through a ring buffer and may not be collected synchronously
* C.8: It would be useful to explain the lookahead and leftbehind parameters - what is the impact of changing them, how should they be set, instead of describe Async IO in detail
* C.9: Provide more background on the 6 SC workloads
* C.10: Why configurations are changed thorugh the evaluation
* C.11: Fix typos

# TODO
1. Run experiments in a larger scale
	1. Use a better version of EMP-Toolkit
	2. Use the new machine
	3. Idea: Use another SMPC protocal in SEAL
	4. Idea: Find implementations of Secure Inference and try
2. Adapt MPK for better multithreading
3. Fix issues mentioned by reviewers in paper

4. Attract the right people (security) by modify the title and the abstract
