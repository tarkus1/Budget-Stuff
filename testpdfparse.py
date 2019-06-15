Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tabula import read_pdf
>>> df =read_pdf("/home/mark/Downloads/451401XXXXXX3663-2019May09-2019Jun10.pdf")
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/tabula/wrapper.py", line 108, in read_pdf
    output = subprocess.check_output(args)
  File "/usr/lib/python3.6/subprocess.py", line 356, in check_output
    **kwargs).stdout
  File "/usr/lib/python3.6/subprocess.py", line 423, in run
    with Popen(*popenargs, **kwargs) as process:
  File "/usr/lib/python3.6/subprocess.py", line 729, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.6/subprocess.py", line 1364, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'java': 'java'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    df =read_pdf("/home/mark/Downloads/451401XXXXXX3663-2019May09-2019Jun10.pdf")
  File "/usr/local/lib/python3.6/dist-packages/tabula/wrapper.py", line 111, in read_pdf
    raise JavaNotFoundError(JAVA_NOT_FOUND_ERROR)
tabula.errors.JavaNotFoundError: `java` command is not found from this Python process. Please ensure Java is installed and PATH is set for `java`
>>> df =read_pdf("/home/mark/Downloads/451401XXXXXX3663-2019May09-2019Jun10.pdf")
>>> df
    MAY 06  MAY 10  ...    -$770.00                                       Unnamed: 4
0      NaN     NaN  ...         NaN                Points adjusted this statement 53
1      NaN     NaN  ...         NaN                                              NaN
2      NaN     NaN  ...         NaN                        New points balance 13,278
3   MAY 08  MAY 10  ...      $57.80                                              NaN
4      NaN     NaN  ...         NaN                                              NaN
5      NaN     NaN  ...         NaN                                       CONTACT US
6   MAY 09  MAY 10  ...       $4.19                                              NaN
7      NaN     NaN  ...         NaN  Customer Service / Lost & Stolen 1-800-769-2512
8      NaN     NaN  ...         NaN                                              NaN
9      NaN     NaN  ...         NaN     Collect Outside North America (416) 974-7780
10  MAY 09  MAY 13  ...      $10.82                                              NaN
11     NaN     NaN  ...         NaN     RBC Rewards Travel Redemption 1-877-636-2870
12     NaN     NaN  ...         NaN                                              NaN
13     NaN     NaN  ...         NaN            Merchandise Redemption 1-800-769-2512
14  MAY 09  MAY 13  ...       $5.00                                              NaN
15     NaN     NaN  ...         NaN                      Web site www.rbcrewards.com
16     NaN     NaN  ...         NaN                                              NaN
17  MAY 09  MAY 13  ...     $200.00                                              NaN
18     NaN     NaN  ...         NaN                        PAYMENTS & INTEREST RATES
19     NaN     NaN  ...         NaN                                              NaN
20     NaN     NaN  ...         NaN                           Minimum payment $10.00
21  MAY 09  MAY 09  ...  -$2,600.00                                              NaN
22     NaN     NaN  ...         NaN                    Payment due date JUL 02, 2019
23     NaN     NaN  ...         NaN                                              NaN
24     NaN     NaN  ...         NaN                          Credit limit $10,000.00
25  MAY 09  MAY 10  ...   $2,600.00                                              NaN
26     NaN     NaN  ...         NaN                           Available credit $0.00
27     NaN     NaN  ...         NaN                                              NaN
28     NaN     NaN  ...         NaN                           Annual interest rates:
29  MAY 10  MAY 13  ...      $39.67                                              NaN
30     NaN     NaN  ...         NaN                                 Purchases 19.99%
31     NaN     NaN  ...         NaN                                              NaN
32     NaN     NaN  ...         NaN                             Cash advances 22.99%
33  MAY 10  MAY 13  ...       $4.70                                              NaN
34     NaN     NaN  ...         NaN                                              NaN
35     NaN     NaN  ...         NaN                         CALCULATING YOUR BALANCE
36  MAY 10  MAY 13  ...     $210.71                                              NaN
37     NaN     NaN  ...         NaN             Previous Statement Balance $7,624.55
38     NaN     NaN  ...         NaN                                              NaN
39     NaN     NaN  ...         NaN                   Payments & credits -$10,370.00
40  MAY 12  MAY 14  ...      $32.55                                              NaN
41     NaN     NaN  ...         NaN                    Purchases & debits $12,952.77
42     NaN     NaN  ...         NaN                                              NaN
43     NaN     NaN  ...         NaN                              Cash advances $0.00
44  MAY 12  MAY 13  ...      $36.62                                              NaN
45     NaN     NaN  ...         NaN                                   Interest $0.00
46     NaN     NaN  ...         NaN                                              NaN
47     NaN     NaN  ...         NaN                                      Fees $29.00
48  MAY 12  MAY 13  ...      $47.30                                              NaN
49     NaN     NaN  ...         NaN                                              NaN
50  MAY 13  MAY 14  ...     $105.00                           NEW BALANCE $10,236.32

[51 rows x 5 columns]
>>> df.describe
<bound method NDFrame.describe of     MAY 06  MAY 10  ...    -$770.00                                       Unnamed: 4
0      NaN     NaN  ...         NaN                Points adjusted this statement 53
1      NaN     NaN  ...         NaN                                              NaN
2      NaN     NaN  ...         NaN                        New points balance 13,278
3   MAY 08  MAY 10  ...      $57.80                                              NaN
4      NaN     NaN  ...         NaN                                              NaN
5      NaN     NaN  ...         NaN                                       CONTACT US
6   MAY 09  MAY 10  ...       $4.19                                              NaN
7      NaN     NaN  ...         NaN  Customer Service / Lost & Stolen 1-800-769-2512
8      NaN     NaN  ...         NaN                                              NaN
9      NaN     NaN  ...         NaN     Collect Outside North America (416) 974-7780
10  MAY 09  MAY 13  ...      $10.82                                              NaN
11     NaN     NaN  ...         NaN     RBC Rewards Travel Redemption 1-877-636-2870
12     NaN     NaN  ...         NaN                                              NaN
13     NaN     NaN  ...         NaN            Merchandise Redemption 1-800-769-2512
14  MAY 09  MAY 13  ...       $5.00                                              NaN
15     NaN     NaN  ...         NaN                      Web site www.rbcrewards.com
16     NaN     NaN  ...         NaN                                              NaN
17  MAY 09  MAY 13  ...     $200.00                                              NaN
18     NaN     NaN  ...         NaN                        PAYMENTS & INTEREST RATES
19     NaN     NaN  ...         NaN                                              NaN
20     NaN     NaN  ...         NaN                           Minimum payment $10.00
21  MAY 09  MAY 09  ...  -$2,600.00                                              NaN
22     NaN     NaN  ...         NaN                    Payment due date JUL 02, 2019
23     NaN     NaN  ...         NaN                                              NaN
24     NaN     NaN  ...         NaN                          Credit limit $10,000.00
25  MAY 09  MAY 10  ...   $2,600.00                                              NaN
26     NaN     NaN  ...         NaN                           Available credit $0.00
27     NaN     NaN  ...         NaN                                              NaN
28     NaN     NaN  ...         NaN                           Annual interest rates:
29  MAY 10  MAY 13  ...      $39.67                                              NaN
30     NaN     NaN  ...         NaN                                 Purchases 19.99%
31     NaN     NaN  ...         NaN                                              NaN
32     NaN     NaN  ...         NaN                             Cash advances 22.99%
33  MAY 10  MAY 13  ...       $4.70                                              NaN
34     NaN     NaN  ...         NaN                                              NaN
35     NaN     NaN  ...         NaN                         CALCULATING YOUR BALANCE
36  MAY 10  MAY 13  ...     $210.71                                              NaN
37     NaN     NaN  ...         NaN             Previous Statement Balance $7,624.55
38     NaN     NaN  ...         NaN                                              NaN
39     NaN     NaN  ...         NaN                   Payments & credits -$10,370.00
40  MAY 12  MAY 14  ...      $32.55                                              NaN
41     NaN     NaN  ...         NaN                    Purchases & debits $12,952.77
42     NaN     NaN  ...         NaN                                              NaN
43     NaN     NaN  ...         NaN                              Cash advances $0.00
44  MAY 12  MAY 13  ...      $36.62                                              NaN
45     NaN     NaN  ...         NaN                                   Interest $0.00
46     NaN     NaN  ...         NaN                                              NaN
47     NaN     NaN  ...         NaN                                      Fees $29.00
48  MAY 12  MAY 13  ...      $47.30                                              NaN
49     NaN     NaN  ...         NaN                                              NaN
50  MAY 13  MAY 14  ...     $105.00                           NEW BALANCE $10,236.32

[51 rows x 5 columns]>
>>> 
