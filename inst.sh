#!/bin/bash


set -x
rm -rf autom4te.cache  
mkdir m4  
aclocal  
autoreconf -i  
automake --add-missing  
autoconf  

RASPA_DIR="`pwd`"
./configure --prefix=${RASPA_DIR}  
# or ./scripts/CompileScript/make-gcc-local  

make  
make install  

