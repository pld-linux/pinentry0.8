
#
# todo:
# - packages with Gtk+ and Qt PIN entry dialogs
#

Summary:	Simple PIN or passphrase entry dialogs
Summary(pl):	Proste kontrolki dialogowe do wpisywania PIN-�w lub hase�
Name:		pinentry
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
URL:		http://www.gnupg.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

%description -l pl
Jest to zestaw prostych kontrolek dialogowych do wpisywania PIN-�w lub
hase�, u�ywaj�ce protoko�u Assuan opisanego w projekcie aegypten;
wi�cej szczegu��w pod adresem http://www.gnupg.org/aegypten/.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/ncurses"
export CPPFLAGS
%configure \
	--disable-pinentry-gtk \
	--disable-pinentry-qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
