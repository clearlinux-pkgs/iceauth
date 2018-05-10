#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iceauth
Version  : 1.0.8
Release  : 12
URL      : http://xorg.freedesktop.org/releases/individual/app/iceauth-1.0.8.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/iceauth-1.0.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT-Opengroup
Requires: iceauth-bin
Requires: iceauth-doc
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE.   It operates very much
like the xauth program for X11 connection authentication records.

%package bin
Summary: bin components for the iceauth package.
Group: Binaries

%description bin
bin components for the iceauth package.


%package doc
Summary: doc components for the iceauth package.
Group: Documentation

%description doc
doc components for the iceauth package.


%prep
%setup -q -n iceauth-1.0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521136680
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1521136680
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iceauth

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
