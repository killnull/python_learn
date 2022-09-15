# encoding:utf-8
print("""
        控制文件读写内容的模式：t和b
            强调：t和b不能单独使用，必须跟r/w/a连用

            t文本（默认的模式）
                1、读写都以str（unicode）为单位的
                2、文本文件
                3、必须指定encoding='utf-8'

            b二进制/bytes

        控制文件读写操作的模式
            r只读模式
            w只写模式
            a只追加写模式
            +：r+、w+、a+
""")