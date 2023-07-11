%define modname	Error
%define modver 0.17026

Summary:	Error/exception handling in an OO-ish way
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/Error-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl-JSON-PP

%description
The Error package provides two interfaces. Firstly Error
provides a procedural interface to exception handling.
Secondly Error is a base class for errors/exceptions that
can either be thrown, for subsequent catch, or can simply
be recorded.
Errors in the class Error should not be thrown directly,
but the user should throw errors from a sub-class of Error.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README examples
%{perl_vendorlib}/Error
%{perl_vendorlib}/Error.pm
%{_mandir}/man3/*



