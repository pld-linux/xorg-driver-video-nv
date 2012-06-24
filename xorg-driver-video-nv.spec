Summary:	X.org video driver for NVIDIA video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych NVIDIA
Name:		xorg-driver-video-nv
Version:	2.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
# Source0-md5:	bbcf04a6b1b95c16bd9fa91e80cc5e43
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1.3
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-nv < 1:7.0.0
Obsoletes:	XFree86-NVidia
Obsoletes:	XFree86-driver-nv < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for NVIDIA video adapters. It supports PCI and AGP
video cards based on the following chips: RIVA 128 (NV3), RIVA TNT
(NV4), RIVA TNT2 (NV5), GeForce 256, QUADRO (NV10), GeForce2, QUADRO2
(NV11, NV15), GeForce3, QUADRO DCC (NV20), nForce, nForce2 (NV1A,
NV1F), GeForce4, QUADRO4 (NV17, NV18, NV25, NV28), GeForce FX, QUADRO
FX (NV30, NV31, NV34, NV35, NV36, NV37, NV38), GeForce 6xxx (NV40,
NV41, NV43, NV44, NV45, C51), GeForce 7xxx (G70, G71, G72, G73).

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych NVIDIA. Obsługuje karty
PCI i AGP oparte na następujących układach: RIVA 128 (NV3), RIVA TNT
(NV4), RIVA TNT2 (NV5), GeForce 256, QUADRO (NV10), GeForce2, QUADRO2
(NV11, NV15), GeForce3, QUADRO DCC (NV20), nForce, nForce2 (NV1A,
NV1F), GeForce4, QUADRO4 (NV17, NV18, NV25, NV28), GeForce FX, QUADRO
FX (NV30, NV31, NV34, NV35, NV36, NV37, NV38), GeForce 6xxx (NV40,
NV41, NV43, NV44, NV45, C51), GeForce 7xxx (G70, G71, G72, G73).

%prep
%setup -q -n xf86-video-nv-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.NV1
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv.4*
