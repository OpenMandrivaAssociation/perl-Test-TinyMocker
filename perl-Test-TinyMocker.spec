%define upstream_name    Test-TinyMocker
Name:		perl-%{upstream_name}
Version:	0.05
Release:	5

Summary:	A very simple tool to mock external modules
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/sukria/Test-TinyMocker/wiki
Source0:	https://cpan.metacpan.org/authors/id/S/SU/SUKRIA/Test-TinyMocker-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 657847
- rebuild for updated spec-helper

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1
+ Revision: 636177
- import perl-Test-TinyMocker



