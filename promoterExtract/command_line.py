import sys
#from promoterExtract import promoter

def sub_usage(args):
    if len(args) == 1:
        print("         \033[1;33;40m\nUsage  :\033[1m\033[1;35;40m  %s\033[1m" %s (args[0]) )
    elif len(args) == 2:
        print("         \033[1;35;40m%s\033[0m    \033[1;32;40m%s\033[0m" % (args[0], args[1]) )

def main_usage():
    print("\n\033[1;33;40mProgram: \033[0m\033[1;35;40m get_promoter \033[1;31;40m(pipeline for promoter extract)\033[0m")
    print("\033[1;33;40mVersion: \033[0m\033[1;32;40m 0.9.5\033[0m")
    print("\033[1;33;40mContact: \033[0m\033[1;32;40m Sitao Zhu <zhusitao1990@163.com>\033[0m")
    print("\033[1;33;40mUsage  : \033[0m\033[1;35;40m get_promoter\033[0m \033[1;31;40m<command>\033[0m")
    print("\033[1;33;40mCommand: \033[0m")
    sub_usage(["create", "create database for GTF or GFF"])
    sub_usage(["extract", "extract promoter for genome or gene"])
    sys.exit(1)


def main():
    if len(sys.argv) == 1:
        main_usage()
    elif len(sys.argv) >= 2:
        if sys.argv[1] in ['create','extract']:
            # import 就执行promoter()
            from promoterExtract import promoter
        else:
            main_usage()

if __name__ == "__main__":
    main()
