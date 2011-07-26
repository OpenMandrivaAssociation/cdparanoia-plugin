%define name cdparanoia-plugin
%define version 0.1
%define release %mkrel 14

Summary: Digital CD playback plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
#gw ignore the results of the cdparanoia configure check
Patch0: cdparanoia-plugin-0.1-configure-check.patch
URL: http://www02.u-page.so-net.ne.jp/ca2/kzmi/xmms/
License: GPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxmms-devel
BuildRequires: libcdda-devel
BuildRequires: automake
Requires: xmms

%description
This plugin reads CDDA sectors and passes them to XMMS directly. That
way you don't need a cable from the CD-ROM to the sound card and you
can use the usual effect and visualization plugins.

%prep
%setup -q
%apply_patches
aclocal
autoconf
automake -a --foreign
libtoolize --force

%build
export LDFLAGS=-lm
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Input/libcdparanoia.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_libdir/xmms/Input/libcdparanoia.so


