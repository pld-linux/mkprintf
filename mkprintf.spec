Summary:	Wraps any text file to a C function that outputs the text
Summary(pl):	Zamienia plik tekstowy na funkcjê C drukuj±c± ten tekst
Name:		mkprintf
Version:	1.0
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/compiler-tools/%{name}-%{version}.tgz
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mkprintf reads the named input file (or standard input if no file is
named) and writes a C function that outputs the text of this file.
This is what lazy C programmers have been waiting for.

%description -l pl
Mkprintf wczytuje podany plik (lub standardowe wej¶cie) i wypisuje
funkcjê w C, która wypisze podany tekst. Typowe narzêdzie dla leniwych
programistów.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} -DVERSION=%{version}" \

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install mkprintf $RPM_BUILD_ROOT%{_bindir}/mkprintf
install mkprintf.8 $RPM_BUILD_ROOT%{_mandir}/man8/mkprintf.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%doc COPYING README
