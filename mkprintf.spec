Summary:	Wraps any text file to a C function that outputs the text
Summary(pl.UTF-8):	Zamienia plik tekstowy na funkcję C drukującą ten tekst
Name:		mkprintf
Version:	1.0
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/compiler-tools/%{name}-%{version}.tgz
# Source0-md5:	2f8e251ede493aa06ab16501c3241cd6
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mkprintf reads the named input file (or standard input if no file is
named) and writes a C function that outputs the text of this file.
This is what lazy C programmers have been waiting for.

%description -l pl.UTF-8
Mkprintf wczytuje podany plik (lub standardowe wejście) i wypisuje
funkcję w C, która wypisze podany tekst. Typowe narzędzie dla leniwych
programistów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DVERSION=%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install mkprintf $RPM_BUILD_ROOT%{_bindir}/mkprintf
install mkprintf.8 $RPM_BUILD_ROOT%{_mandir}/man8/mkprintf.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
