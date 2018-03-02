set -e

cd pkg-src
wget -c https://ftp.gnu.org/gnu/bash/bash-4.4.18.tar.gz
wget -c https://ftp.gnu.org/gnu/coreutils/coreutils-8.29.tar.xz
wget -c https://ftp.gnu.org/gnu/cpio/cpio-2.12.tar.gz
wget -c https://ftp.gnu.org/gnu/diffutils/diffutils-3.6.tar.xz
wget -c https://ftp.gnu.org/gnu/findutils/findutils-4.6.0.tar.gz
wget -c https://ftp.gnu.org/gnu/grep/grep-3.1.tar.xz
wget -c https://ftp.gnu.org/gnu/groff/groff-1.22.3.tar.gz
wget -c https://ftp.gnu.org/gnu/gzip/gzip-1.9.tar.gz
wget -c https://ftp.gnu.org/gnu/inetutils/inetutils-1.9.4.tar.gz
wget -c https://ftp.gnu.org/gnu/plotutils/plotutils-2.6.tar.gz
wget -c https://ftp.gnu.org/gnu/readline/readline-7.0.tar.gz
wget -c https://ftp.gnu.org/gnu/screen/screen-4.6.2.tar.gz
wget -c https://ftp.gnu.org/gnu/tar/tar-1.30.tar.xz
wget -c https://ftp.gnu.org/gnu/texinfo/texinfo-6.5.tar.gz
wget -c https://ftp.gnu.org/gnu/time/time-1.8.tar.gz

wget -c https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
wget -c https://ftp.gnu.org/gnu/automake/automake-1.15.1.tar.gz
wget -c --no-check-certificate https://sydneyerickson.me/stuff/bison-3.0.4.tar.gz
wget -c https://www.samba.org/ftp/ccache/ccache-3.3.6.tar.gz
wget -c https://ftp.gnu.org/gnu/make/make-4.2.1.tar.gz
wget -c https://cmake.org/files/v3.10/cmake-3.10.2.tar.gz
wget -c https://ftp.gnu.org/gnu/gawk/gawk-4.2.0.tar.gz
wget -c https://codeload.github.com/git/git/tar.gz/v2.16.1 -O git-2.16.1.tar.gz
wget -c https://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.gz
wget -c https://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.gz
wget -c https://www.mercurial-scm.org/release/mercurial-4.4.2.tar.gz
wget -c https://download.mono-project.com/sources/mono/mono-5.4.1.7.tar.bz2
wget -c http://www.nasm.us/pub/nasm/releasebuilds/2.13.02/nasm-2.13.02.tar.gz
wget -c https://static.rust-lang.org/dist/rustc-1.23.0-src.tar.gz
wget -c http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
wget -c https://codeload.github.com/dlang/dmd/tar.gz/v2.078.1 -O dmd-2.078.1.tar.gz
wget -c https://codeload.github.com/ninja-build/ninja/tar.gz/v1.8.2 -O ninja-1.8.2.tar.gz

wget -c https://ftp.gnu.org/gnu/gmp/gmp-6.1.2.tar.bz2
wget -c https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz
wget -c https://ftp.gnu.org/gnu/mpfr/mpfr-4.0.0.tar.gz
wget -c http://isl.gforge.inria.fr/isl-0.18.tar.gz
wget -c http://www.bastoul.net/cloog/pages/download/cloog-0.18.4.tar.gz
wget -c https://ftp.gnu.org/gnu/binutils/binutils-2.30.tar.gz
wget -c https://ftp.gnu.org/gnu/gcc/gcc-7.3.0/gcc-7.3.0.tar.gz

# LLVM