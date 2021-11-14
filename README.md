# The problem
In this project I have tried to sort all given phone numbers (+79-XXX-XXX-XXX) from huge file on disk. One line contains one phone, without any other delimeters.


# Preparations
I used my pc with AMD Ryzen 7 3700X 8-Core Processor for all the tests.

### create venv for python's scripts

```bash
python3 -m venv venv
$./venv/bin/python -m pip install -U pip setuptools wheel
$./venv/bin/python -m pip install -r requirements.txt
```

### gen some file with pseudo-random phones for test
##### WARNING: The file requires 13G on disk.
For simplicity, lets just write phone numbers in the reverse order, it will not affect the solution.
I tried to generate a file with C++, Python and Rust just for fun.
Implementation in Rust happens to be the fastest, it looks like it can handle buffering better.
(I put the amd64 compiled linux binary to this repo to rs/rs)

```bash
$ gcc gen.cpp -lstdc++ -o gen
$ time ./gen /media/data/temp/phones.txt
./gen /media/data/temp/c_phones.txt  61.64s user 6.31s system 69% cpu 1:37.94 total
# -O2 and -O3 doens't give any noticeable boost
#---------------------------------------------------------------------
$ time venv/bin/python gen.py --path /media/data/temp/phones.txt
venv/bin/python gen.py --path /media/data/temp/phones.txt  260.93s user 7.53s system 98% cpu 4:33.11 total
#---------------------------------------------------------------------
$ time cargo run --release  -- /media/data/temp/phones.txt
cargo run --release -- /media/data/temp/phones.txt  34.42s user 5.81s system 38% cpu 1:44.87 total
```

# Sorting the file
Because of huge amount of input data lets sort the file using [external sort algorithm](https://en.wikipedia.org/wiki/External_sorting).
There is a nice [python implementation](https://github.com/dapper91/python-external-sort).
Note: Addition disk space is required for chunks(size of size can be specified)

sort.py reads chunks from input_path/phones.txt using multiprocessing, sorts them and then merges using heap. Result is written into input_path/sorted.txt.
script finished in 24.5 min

```bash
time ./venv/bin/python sort.py --path /media/data/temp --chunk_size 10000000
[DEBUG   ] 2021-11-06 14:23:59,517 (ext_sort): sorting file using 16 workers (chunk_size: 10000000)
[DEBUG   ] 2021-11-06 14:23:59,517 (ext_sort): using '/media/data/temp/tmp1auyejpe' as temporary directory
[DEBUG   ] 2021-11-06 14:24:01,994 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-ehaqdvi4'...
[DEBUG   ] 2021-11-06 14:24:03,862 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-ehaqdvi4'...
[DEBUG   ] 2021-11-06 14:24:06,356 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-g25v1xcd'...
[DEBUG   ] 2021-11-06 14:24:08,267 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-g25v1xcd'...
[DEBUG   ] 2021-11-06 14:24:10,759 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-_xbqt3xt'...
[DEBUG   ] 2021-11-06 14:24:12,654 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-_xbqt3xt'...
[DEBUG   ] 2021-11-06 14:24:15,152 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-lv5r_9en'...
[DEBUG   ] 2021-11-06 14:24:17,082 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-lv5r_9en'...
[DEBUG   ] 2021-11-06 14:24:19,586 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-o4yfgc0d'...
[DEBUG   ] 2021-11-06 14:24:21,487 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-o4yfgc0d'...
[DEBUG   ] 2021-11-06 14:24:23,993 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-tysg61ui'...
[DEBUG   ] 2021-11-06 14:24:25,898 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-tysg61ui'...
[DEBUG   ] 2021-11-06 14:24:28,402 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-evnnkewx'...
[DEBUG   ] 2021-11-06 14:24:30,303 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-evnnkewx'...
[DEBUG   ] 2021-11-06 14:24:32,810 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-gvfv1i03'...
[DEBUG   ] 2021-11-06 14:24:34,713 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-gvfv1i03'...
[DEBUG   ] 2021-11-06 14:24:37,212 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-hinusheh'...
[DEBUG   ] 2021-11-06 14:24:39,226 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-hinusheh'...
[DEBUG   ] 2021-11-06 14:24:41,728 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-wzakfrf5'...
[DEBUG   ] 2021-11-06 14:24:43,642 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-wzakfrf5'...
[DEBUG   ] 2021-11-06 14:24:46,136 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-uknoepz4'...
[DEBUG   ] 2021-11-06 14:24:48,046 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-uknoepz4'...
[DEBUG   ] 2021-11-06 14:24:50,545 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-esiysv8b'...
[DEBUG   ] 2021-11-06 14:24:52,453 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-esiysv8b'...
[DEBUG   ] 2021-11-06 14:24:54,956 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-rcjmppts'...
[DEBUG   ] 2021-11-06 14:24:56,853 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-rcjmppts'...
[DEBUG   ] 2021-11-06 14:24:59,384 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-ua7fc1fx'...
[DEBUG   ] 2021-11-06 14:25:01,320 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-ua7fc1fx'...
[DEBUG   ] 2021-11-06 14:25:03,850 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-xqs6836_'...
[DEBUG   ] 2021-11-06 14:25:05,841 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-xqs6836_'...
[DEBUG   ] 2021-11-06 14:25:08,372 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-tjttnp28'...
[DEBUG   ] 2021-11-06 14:25:10,317 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-tjttnp28'...
[DEBUG   ] 2021-11-06 14:25:12,817 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-f1a7y4z0'...
[DEBUG   ] 2021-11-06 14:25:14,765 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-f1a7y4z0'...
[DEBUG   ] 2021-11-06 14:25:17,270 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-aplgdoh3'...
[DEBUG   ] 2021-11-06 14:25:19,461 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-aplgdoh3'...
[DEBUG   ] 2021-11-06 14:25:21,909 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-el7wxe4i'...
[DEBUG   ] 2021-11-06 14:25:23,846 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-el7wxe4i'...
[DEBUG   ] 2021-11-06 14:25:26,356 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-7848uahn'...
[DEBUG   ] 2021-11-06 14:25:28,279 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-7848uahn'...
[DEBUG   ] 2021-11-06 14:25:30,809 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-aqbxfazv'...
[DEBUG   ] 2021-11-06 14:25:32,730 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-aqbxfazv'...
[DEBUG   ] 2021-11-06 14:25:35,255 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-rmw7pif0'...
[DEBUG   ] 2021-11-06 14:25:37,197 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-rmw7pif0'...
[DEBUG   ] 2021-11-06 14:25:39,715 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-sj9dli_k'...
[DEBUG   ] 2021-11-06 14:25:41,646 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-sj9dli_k'...
[DEBUG   ] 2021-11-06 14:25:44,177 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-k3zac5re'...
[DEBUG   ] 2021-11-06 14:25:46,145 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-k3zac5re'...
[DEBUG   ] 2021-11-06 14:25:48,661 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-t4sawii7'...
[DEBUG   ] 2021-11-06 14:25:50,596 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-t4sawii7'...
[DEBUG   ] 2021-11-06 14:25:53,114 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-u7pbcw89'...
[DEBUG   ] 2021-11-06 14:25:55,046 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-u7pbcw89'...
[DEBUG   ] 2021-11-06 14:25:57,556 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-imq4f4pz'...
[DEBUG   ] 2021-11-06 14:25:59,490 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-imq4f4pz'...
[DEBUG   ] 2021-11-06 14:26:02,004 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-sbcmrli8'...
[DEBUG   ] 2021-11-06 14:26:03,960 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-sbcmrli8'...
[DEBUG   ] 2021-11-06 14:26:06,488 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-uy4nsfhg'...
[DEBUG   ] 2021-11-06 14:26:08,430 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-uy4nsfhg'...
[DEBUG   ] 2021-11-06 14:26:10,946 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-q4pw25y7'...
[DEBUG   ] 2021-11-06 14:26:12,882 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-q4pw25y7'...
[DEBUG   ] 2021-11-06 14:26:15,400 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-4j3nkwbe'...
[DEBUG   ] 2021-11-06 14:26:17,334 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-4j3nkwbe'...
[DEBUG   ] 2021-11-06 14:26:19,861 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-o5d14uc4'...
[DEBUG   ] 2021-11-06 14:26:21,791 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-o5d14uc4'...
[DEBUG   ] 2021-11-06 14:26:24,303 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-y9o_2f3w'...
[DEBUG   ] 2021-11-06 14:26:26,233 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-y9o_2f3w'...
[DEBUG   ] 2021-11-06 14:26:28,754 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-vemn_lcm'...
[DEBUG   ] 2021-11-06 14:26:30,760 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-vemn_lcm'...
[DEBUG   ] 2021-11-06 14:26:33,306 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-nfg4e_ah'...
[DEBUG   ] 2021-11-06 14:26:35,236 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-nfg4e_ah'...
[DEBUG   ] 2021-11-06 14:26:37,771 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-s80_mwjv'...
[DEBUG   ] 2021-11-06 14:26:39,761 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-s80_mwjv'...
[DEBUG   ] 2021-11-06 14:26:42,275 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-2evwo6xd'...
[DEBUG   ] 2021-11-06 14:26:44,208 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-2evwo6xd'...
[DEBUG   ] 2021-11-06 14:26:46,736 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-ygg7svrj'...
[DEBUG   ] 2021-11-06 14:26:48,674 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-ygg7svrj'...
[DEBUG   ] 2021-11-06 14:26:51,191 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-46_9u6jf'...
[DEBUG   ] 2021-11-06 14:26:53,121 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-46_9u6jf'...
[DEBUG   ] 2021-11-06 14:26:55,643 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-86jw13yt'...
[DEBUG   ] 2021-11-06 14:26:57,636 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-86jw13yt'...
[DEBUG   ] 2021-11-06 14:27:00,153 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-gysfz691'...
[DEBUG   ] 2021-11-06 14:27:02,078 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-gysfz691'...
[DEBUG   ] 2021-11-06 14:27:04,606 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-3zk8d06g'...
[DEBUG   ] 2021-11-06 14:27:06,576 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-3zk8d06g'...
[DEBUG   ] 2021-11-06 14:27:09,110 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-rt2xq5hp'...
[DEBUG   ] 2021-11-06 14:27:11,045 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-rt2xq5hp'...
[DEBUG   ] 2021-11-06 14:27:13,571 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-rhkv4jt6'...
[DEBUG   ] 2021-11-06 14:27:15,504 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-rhkv4jt6'...
[DEBUG   ] 2021-11-06 14:27:18,024 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-lpqgo9za'...
[DEBUG   ] 2021-11-06 14:27:19,958 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-lpqgo9za'...
[DEBUG   ] 2021-11-06 14:27:22,475 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-hmjlr5ab'...
[DEBUG   ] 2021-11-06 14:27:24,538 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-hmjlr5ab'...
[DEBUG   ] 2021-11-06 14:27:26,984 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-wbasmfuu'...
[DEBUG   ] 2021-11-06 14:27:28,994 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-wbasmfuu'...
[DEBUG   ] 2021-11-06 14:27:31,502 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-k_5uu61l'...
[DEBUG   ] 2021-11-06 14:27:33,418 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-k_5uu61l'...
[DEBUG   ] 2021-11-06 14:27:35,947 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-w2h9lji6'...
[DEBUG   ] 2021-11-06 14:27:37,866 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-w2h9lji6'...
[DEBUG   ] 2021-11-06 14:27:40,395 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-e9whnyiy'...
[DEBUG   ] 2021-11-06 14:27:42,487 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-e9whnyiy'...
[DEBUG   ] 2021-11-06 14:27:44,861 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-dyrfax5x'...
[DEBUG   ] 2021-11-06 14:27:46,800 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-dyrfax5x'...
[DEBUG   ] 2021-11-06 14:27:49,309 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-mmu8z_1o'...
[DEBUG   ] 2021-11-06 14:27:51,254 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-mmu8z_1o'...
[DEBUG   ] 2021-11-06 14:27:53,754 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-ikgque7u'...
[DEBUG   ] 2021-11-06 14:27:55,807 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-ikgque7u'...
[DEBUG   ] 2021-11-06 14:27:58,223 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-7hwftjml'...
[DEBUG   ] 2021-11-06 14:28:00,177 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-7hwftjml'...
[DEBUG   ] 2021-11-06 14:28:02,680 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-a7_4kga0'...
[DEBUG   ] 2021-11-06 14:28:04,648 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-a7_4kga0'...
[DEBUG   ] 2021-11-06 14:28:07,147 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-weyv2r1r'...
[DEBUG   ] 2021-11-06 14:28:09,076 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-weyv2r1r'...
[DEBUG   ] 2021-11-06 14:28:11,598 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-x8dnic4l'...
[DEBUG   ] 2021-11-06 14:28:13,814 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-x8dnic4l'...
[DEBUG   ] 2021-11-06 14:28:16,055 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-n3ktklro'...
[DEBUG   ] 2021-11-06 14:28:17,986 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-n3ktklro'...
[DEBUG   ] 2021-11-06 14:28:20,529 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-9jao20h0'...
[DEBUG   ] 2021-11-06 14:28:22,714 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-9jao20h0'...
[DEBUG   ] 2021-11-06 14:28:24,971 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-0c_h7eew'...
[DEBUG   ] 2021-11-06 14:28:26,888 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-0c_h7eew'...
[DEBUG   ] 2021-11-06 14:28:29,409 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-1otper8b'...
[DEBUG   ] 2021-11-06 14:28:31,349 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-1otper8b'...
[DEBUG   ] 2021-11-06 14:28:33,826 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-uik8ludu'...
[DEBUG   ] 2021-11-06 14:28:35,722 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-uik8ludu'...
[DEBUG   ] 2021-11-06 14:28:38,218 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-t5wi75xy'...
[DEBUG   ] 2021-11-06 14:28:40,118 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-t5wi75xy'...
[DEBUG   ] 2021-11-06 14:28:42,637 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-fzpnrmmk'...
[DEBUG   ] 2021-11-06 14:28:44,546 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-fzpnrmmk'...
[DEBUG   ] 2021-11-06 14:28:47,063 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-pr43w89a'...
[DEBUG   ] 2021-11-06 14:28:49,036 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-pr43w89a'...
[DEBUG   ] 2021-11-06 14:28:51,532 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-8hwq9yah'...
[DEBUG   ] 2021-11-06 14:28:53,436 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-8hwq9yah'...
[DEBUG   ] 2021-11-06 14:28:55,938 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-w29er1is'...
[DEBUG   ] 2021-11-06 14:28:57,977 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-w29er1is'...
[DEBUG   ] 2021-11-06 14:29:00,480 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-rxq5vw2d'...
[DEBUG   ] 2021-11-06 14:29:02,475 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-rxq5vw2d'...
[DEBUG   ] 2021-11-06 14:29:04,983 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-2om0covw'...
[DEBUG   ] 2021-11-06 14:29:06,896 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-2om0covw'...
[DEBUG   ] 2021-11-06 14:29:09,409 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-lr6426er'...
[DEBUG   ] 2021-11-06 14:29:11,326 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-lr6426er'...
[DEBUG   ] 2021-11-06 14:29:13,905 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-oez_22sv'...
[DEBUG   ] 2021-11-06 14:29:15,818 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-oez_22sv'...
[DEBUG   ] 2021-11-06 14:29:22,153 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-_htbwrao'...
[DEBUG   ] 2021-11-06 14:29:24,050 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-_htbwrao'...
[DEBUG   ] 2021-11-06 14:29:34,476 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-nmz9s3zq'...
[DEBUG   ] 2021-11-06 14:29:36,349 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-nmz9s3zq'...
[DEBUG   ] 2021-11-06 14:29:43,407 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-q3mvqia9'...
[DEBUG   ] 2021-11-06 14:29:45,361 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-q3mvqia9'...
[DEBUG   ] 2021-11-06 14:29:49,787 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-gnnws1aa'...
[DEBUG   ] 2021-11-06 14:29:51,650 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-gnnws1aa'...
[DEBUG   ] 2021-11-06 14:29:57,098 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-mrvgb22h'...
[DEBUG   ] 2021-11-06 14:29:58,965 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-mrvgb22h'...
[DEBUG   ] 2021-11-06 14:30:02,683 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-q3rl0op9'...
[DEBUG   ] 2021-11-06 14:30:04,554 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-q3rl0op9'...
[DEBUG   ] 2021-11-06 14:30:08,240 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-jcyxwsw0'...
[DEBUG   ] 2021-11-06 14:30:10,109 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-jcyxwsw0'...
[DEBUG   ] 2021-11-06 14:30:12,726 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-94j_6srr'...
[DEBUG   ] 2021-11-06 14:30:14,620 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-94j_6srr'...
[DEBUG   ] 2021-11-06 14:30:17,433 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-inctz241'...
[DEBUG   ] 2021-11-06 14:30:19,329 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-inctz241'...
[DEBUG   ] 2021-11-06 14:30:24,767 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-m3hf41ik'...
[DEBUG   ] 2021-11-06 14:30:26,637 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-m3hf41ik'...
[DEBUG   ] 2021-11-06 14:30:35,566 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-q8pz7y3v'...
[DEBUG   ] 2021-11-06 14:30:37,438 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-q8pz7y3v'...
[DEBUG   ] 2021-11-06 14:30:40,048 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-yckuvped'...
[DEBUG   ] 2021-11-06 14:30:41,953 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-yckuvped'...
[DEBUG   ] 2021-11-06 14:30:45,315 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-hzcpwg07'...
[DEBUG   ] 2021-11-06 14:30:47,252 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-hzcpwg07'...
[DEBUG   ] 2021-11-06 14:30:58,651 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-g1jontcm'...
[DEBUG   ] 2021-11-06 14:31:00,519 (ext_sort): [ForkPoolWorker-5] sorting file '/media/data/temp/tmp1auyejpe/chunk-g1jontcm'...
[DEBUG   ] 2021-11-06 14:31:04,455 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-t3gbmymr'...
[DEBUG   ] 2021-11-06 14:31:06,394 (ext_sort): [ForkPoolWorker-6] sorting file '/media/data/temp/tmp1auyejpe/chunk-t3gbmymr'...
[DEBUG   ] 2021-11-06 14:31:11,974 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-5co66hcg'...
[DEBUG   ] 2021-11-06 14:31:13,880 (ext_sort): [ForkPoolWorker-7] sorting file '/media/data/temp/tmp1auyejpe/chunk-5co66hcg'...
[DEBUG   ] 2021-11-06 14:31:16,544 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-9llnyf_x'...
[DEBUG   ] 2021-11-06 14:31:18,491 (ext_sort): [ForkPoolWorker-8] sorting file '/media/data/temp/tmp1auyejpe/chunk-9llnyf_x'...
[DEBUG   ] 2021-11-06 14:31:24,722 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-belsq_me'...
[DEBUG   ] 2021-11-06 14:31:26,613 (ext_sort): [ForkPoolWorker-9] sorting file '/media/data/temp/tmp1auyejpe/chunk-belsq_me'...
[DEBUG   ] 2021-11-06 14:31:29,191 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-f9hv8xrb'...
[DEBUG   ] 2021-11-06 14:31:31,131 (ext_sort): [ForkPoolWorker-10] sorting file '/media/data/temp/tmp1auyejpe/chunk-f9hv8xrb'...
[DEBUG   ] 2021-11-06 14:31:38,761 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-f6q0bi9w'...
[DEBUG   ] 2021-11-06 14:31:40,651 (ext_sort): [ForkPoolWorker-11] sorting file '/media/data/temp/tmp1auyejpe/chunk-f6q0bi9w'...
[DEBUG   ] 2021-11-06 14:31:43,876 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-7i0lbcnb'...
[DEBUG   ] 2021-11-06 14:31:45,780 (ext_sort): [ForkPoolWorker-12] sorting file '/media/data/temp/tmp1auyejpe/chunk-7i0lbcnb'...
[DEBUG   ] 2021-11-06 14:31:48,602 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-7brnhm7x'...
[DEBUG   ] 2021-11-06 14:31:50,496 (ext_sort): [ForkPoolWorker-13] sorting file '/media/data/temp/tmp1auyejpe/chunk-7brnhm7x'...
[DEBUG   ] 2021-11-06 14:31:56,840 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-zx0_fqqg'...
[DEBUG   ] 2021-11-06 14:31:58,777 (ext_sort): [ForkPoolWorker-14] sorting file '/media/data/temp/tmp1auyejpe/chunk-zx0_fqqg'...
[DEBUG   ] 2021-11-06 14:32:07,304 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-maytq_eo'...
[DEBUG   ] 2021-11-06 14:32:09,193 (ext_sort): [ForkPoolWorker-15] sorting file '/media/data/temp/tmp1auyejpe/chunk-maytq_eo'...
[DEBUG   ] 2021-11-06 14:32:22,064 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-fjlde6eb'...
[DEBUG   ] 2021-11-06 14:32:23,970 (ext_sort): [ForkPoolWorker-16] sorting file '/media/data/temp/tmp1auyejpe/chunk-fjlde6eb'...
[DEBUG   ] 2021-11-06 14:32:27,400 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-yfh4924m'...
[DEBUG   ] 2021-11-06 14:32:29,315 (ext_sort): [ForkPoolWorker-1] sorting file '/media/data/temp/tmp1auyejpe/chunk-yfh4924m'...
[DEBUG   ] 2021-11-06 14:32:31,876 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-gc_g1_ja'...
[DEBUG   ] 2021-11-06 14:32:33,802 (ext_sort): [ForkPoolWorker-2] sorting file '/media/data/temp/tmp1auyejpe/chunk-gc_g1_ja'...
[DEBUG   ] 2021-11-06 14:32:36,351 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-i54ckt6a'...
[DEBUG   ] 2021-11-06 14:32:38,268 (ext_sort): [ForkPoolWorker-3] sorting file '/media/data/temp/tmp1auyejpe/chunk-i54ckt6a'...
[DEBUG   ] 2021-11-06 14:32:46,721 (ext_sort): creating chunk file '/media/data/temp/tmp1auyejpe/chunk-orh7kgk_'...
[DEBUG   ] 2021-11-06 14:32:48,609 (ext_sort): [ForkPoolWorker-4] sorting file '/media/data/temp/tmp1auyejpe/chunk-orh7kgk_'...
[DEBUG   ] 2021-11-06 14:32:52,540 (ext_sort): merging result...
./venv/bin/python sort.py --path /media/data/temp  1456.58s user 68.46s system 119% cpu 21:19.70 total

```

