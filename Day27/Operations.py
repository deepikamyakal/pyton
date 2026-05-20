# User defined
# import operations

from op import demo

a = int(input("enter a value :"))
b = int(input("enter b value :"))

obj = demo()

option = int(input(' enter 1 for addition ,  enter 2 for subtraction ,  enter 3 for multiplication , enter 4 for division'))
if option ==1:
    print(obj.add(a,b))

elif option ==2:
    print(obj.sub(a,b))

elif option ==3:
    print(obj.mul(a,b))

elif option ==4:
    print(obj.div(a,b))

else:
    print("you have choosen wrong option.")


# help("modules")'''
# __future__          _stat               fileinput                 rlcompleter
# __hello__           _statistics         fnmatch                   runpy
# __phello__          _string             fractions                 sched_abc                
# _strptime           ftplib              secrets_aix_support        
#_struct             functools           select_android_support   
#_suggestions        gc                 selectors_apple_support      
# _symtable           genericpath         shelve_ast                
#_sysconfig          getopt              shlex_ast_unparse       
# _thread             getpass             shutil_asyncio           
# _threading_local    gettext             signal_bisect            
# _tkinter            glob                site_blake2            
# _tokenize           graphlib            smtplib_bz2                
# _tracemalloc        gzip                socket_codecs             
# _types              hashlib             socketserver_codecs_cn          
# _typing             heapq               sqlite3_codecs_hk          
# _uuid               hmac                sqlparse_codecs_iso2022     
# _warnings           html                sre_compile_codecs_jp          
# _weakref            http                sre_constants_codecs_kr          
# _weakrefset         idlelib             sre_parse_codecs_tw          
# _winapi             imaplib             ssl_collections        
# _wmi                importlib           stat_collections_abc    
# _zoneinfo           inspect             statistics_colorize           
# _zstd               io                  string_compat_pickle      
# abc                 ipaddress           stringprep_contextvars        
# annotationlib       itertools           struct_csv                    antigravity         json               
# subprocess_ctypes   argparse            keyword                       symtable_datetime           
# array               linecache           sys_decimal            asgiref             locale             
# sysconfig_elementtree        ast                 logging             tabnanny_functools          
# asyncio             lzma                tarfile_hashlib            atexit              mailbox      
#        tempfile_heapq              base64              marshal             textwrap_hmac             
#   bdb                 math                this_imp                binascii            mimetypes      
#      threading_interpchannels     bisect              mmap                time_interpqueues       
# builtins            modulefinder        timeit_interpreters       bz2                 modules
#              tkinter_io                 cProfile            msvcrt              token_ios_support      
#   calendar            multiprocessing     tokenize_json               cmath               netrc          
#      tomllib_locale             cmd                 nt                  trace_lsprof             code          
#       ntpath              traceback_lzma               codecs              nturl2path          tracemalloc_markupbase      
#    codeop              numbers             tty_md5                collections         opcode             
#  turtle_multibytecodec     colorsys            operator            turtledemo_multiprocessing    compileall        
#   optparse            types_opcode             compression         os                  typing_opcode_metadata   
#  concurrent          pathlib             tzdata_operator           configparser        pdb                
#  unicodedata_osx_support        contextlib          pickle              unittest_overlapped         contextvars        
#  pickletools         urllib_pickle             copy                pip                 uuid_py_abc           
#   copyreg             pkgutil             venv_py_warnings        csv                 platform           
#  warnings_pydatetime         ctypes              plistlib            wave_pydecimal          curses             
#  poplib              weakref_pyio               dataclasses         posixpath           webbrowser_pylong           
#   datetime            pprint              winreg_pyrepl             dbm                 profile            
#  winsound_queue              decimal             pstats              wsgiref_random             difflib          
#  pty                 xml_remote_debugging   dis                 py_compile          xmlrpc_sha1           
#     django              pyclbr              xxsubtype_sha2               doctest            
#  pydoc               zipapp_sha3               email               pydoc_data          zipfile_signal           
#   encodings           pyexpat             zipimport_sitebuiltins       ensurepip           queue              
#  zlib_socket             enum                quopri              zoneinfo_sqlite3            errno              
#  random              _sre                faulthandler        re                  _ssl               
#  filecmp         reprlib  
# '''