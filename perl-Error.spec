%define upstream_name    Error
%define upstream_version 0.17016

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4
Epoch:      1

Summary:    Error/exception handling in an OO-ish way
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The Error package provides two interfaces. Firstly Error
provides a procedural interface to exception handling.
Secondly Error is a base class for errors/exceptions that
can either be thrown, for subsequent catch, or can simply
be recorded.
Errors in the class Error should not be thrown directly,
but the user should throw errors from a sub-class of Error.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
