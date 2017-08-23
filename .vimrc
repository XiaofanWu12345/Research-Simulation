set number
set autoindent
set tabstop=4
set shiftwidth=4
set expandtab
ab psvm public static void main(String[] args)
ab psvM public static void Main(String[] args)
ab sop System.out.print
ab sopl System.out.println
ab sopf System.out.printf
ab cw Console.Write
ab cwl Console.WriteLine
ab cr Console.Read
ab crl Console.ReadLine
ab ip Integer.parseInt
ab dp Double.parseDouble
ab bp Boolean.parseBoolean
ab sf String.format
ab dm def main(args: Array[String])
ab im int main(int argc, char * argv[])
autocmd FileType py,java,c,R,scala,rb,perl,cpp,h,bas,sh,bat,js,html,css,cs autocmd BufWritePre <buffer> %s/\s\+$//e
