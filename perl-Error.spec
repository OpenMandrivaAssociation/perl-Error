%define module  Error
%define name    perl-%{module}
%define version 0.17011
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL or Artistic
Group:          Development/Perl
Summary:        Error/exception handling in an OO-ish way
URL:            http://search.cpan.org/dist/%{module}
Source:         http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/%{module}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The Error package provides two interfaces. Firstly Error
provides a procedural interface to exception handling.
Secondly Error is a base class for errors/exceptions that
can either be thrown, for subsequent catch, or can simply
be recorded.
Errors in the class Error should not be thrown directly,
but the user should throw errors from a sub-class of Error.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README examples
%{perl_vendorlib}/Error
%{perl_vendorlib}/Error.pm
%{_mandir}/*/*

