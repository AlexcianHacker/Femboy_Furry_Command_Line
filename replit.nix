{pkgs}: {
  deps = [
    pkgs.pypy3
    pkgs.pypy
    pkgs.rustc
    pkgs.pkg-config
    pkgs.openssl
    pkgs.libxcrypt
    pkgs.libiconv
    pkgs.cargo
  ];
}
