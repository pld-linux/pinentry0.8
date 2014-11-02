# TODO: use system libassuan 2 instead of included libassuan 1
#
# Conditional build:
%bcond_without	gtk	# without GTK+ 1.x dialog
%bcond_without	qt	# without Qt 3.x dialog
#
Summary:	Simple PIN or passphrase entry dialogs (old frontends)
Summary(pl.UTF-8):	Proste kontrolki dialogowe do wpisywania PIN-ów lub haseł (stare interfejsy)
Name:		pinentry0.8
Version:	0.8.4
Release:	3
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/pinentry/pinentry-%{version}.tar.bz2
# Source0-md5:	e2b6f94471ba1e978f6e5bf6b275189b
Patch0:		pinentry-system-assuan.patch
Patch1:		pinentry-info.patch
Patch2:		pinentry-am.patch
Patch3:		pinentry-doc.patch
Patch4:		pinentry-activate.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel
%{?with_gtk:BuildRequires:	gtk+-devel >= 1.2.0}
#BuildRequires:	libassuan-devel
BuildRequires:	libcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel >= 3}
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

This is an older version of pinentry, the last which contained GTK+
1.x and Qt 3.x based dialogs.

%description -l pl.UTF-8
Jest to zestaw prostych kontrolek dialogowych do wpisywania PIN-ów lub
haseł, używające protokołu Assuan opisanego w projekcie aegypten;
więcej szczegółów pod adresem http://www.gnupg.org/aegypten/.

Ten pakiet to starsza wersja pinentry, ostatnia zawierająca kontrolki
oparte na bibliotekach GTK+ 1.x oraz Qt 3.x

%package -n pinentry-gtk
Summary:	Simple PIN or passphrase entry dialog for GTK+ 1.x
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+ 1.x
Group:		X11/Applications

%description -n pinentry-gtk
Simple PIN or passphrase entry dialog for GTK+ 1.x.

%description -n pinentry-gtk -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla GTK+
1.x.

%package -n pinentry-qt
Summary:	Simple PIN or passphrase entry dialog for Qt 3
Summary(pl.UTF-8):	Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt 3
Group:		X11/Applications

%description -n pinentry-qt
Simple PIN or passphrase entry dialog for Qt 3.

%description -n pinentry-qt -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt 3.

%prep
%setup -q -n pinentry-%{version}
#patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

#%{__rm} assuan/*.h

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--enable-maintainer-mode \
	--enable-pinentry-curses=no \
	--enable-pinentry-gtk%{!?with_gtk:=no} \
	--enable-pinentry-gtk2=no \
	--enable-pinentry-qt%{!?with_qt:=no} \
	--enable-pinentry-qt4=no \
	--enable-pinentry-tty=no \
	--with-qt-includes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/pinentry \
	$RPM_BUILD_ROOT%{_infodir}/pinentry.info

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with gtk}
%files -n pinentry-gtk
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/pinentry-gtk
%endif

%if %{with qt}
%files -n pinentry-qt
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/pinentry-qt
%endif
