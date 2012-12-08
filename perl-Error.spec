%define upstream_name    Error
%define upstream_version 0.17016

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Epoch:		1

Summary:	Error/exception handling in an OO-ish way
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.170.160-4mdv2012.0
+ Revision: 765199
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.170.160-3
+ Revision: 763715
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.170.160-2
+ Revision: 667129
- mass rebuild

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.170.160-1mdv2010.1
+ Revision: 480743
- bumping epoch
- update to 0.17016

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.17015-3mdv2010.0
+ Revision: 426444
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.17015-2mdv2009.1
+ Revision: 351722
- rebuild

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17015-1mdv2009.0
+ Revision: 238991
- update to new version 0.17015

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17014-1mdv2009.0
+ Revision: 212213
- update to new version 0.17014

* Fri May 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17013-1mdv2009.0
+ Revision: 210277
- update to new version 0.17013

* Sat Jan 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17012-1mdv2008.1
+ Revision: 158256
- update to new version 0.17012

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17011-1mdv2008.1
+ Revision: 138045
- update to new version 0.17011

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17010-1mdv2008.1
+ Revision: 111419
- update to new version 0.17010

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17009-1mdv2008.0
+ Revision: 78449
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.17008-1mdv2008.0
+ Revision: 20064
- 0.17008


* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17001-1mdv2007.0
- new version

* Wed Apr 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15009-1mdk
- New release 0.15009

* Thu Apr 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15008-1mdk
- New release 0.15008
- spec cleanup
- %%mkrel
- better summary
- don't ship MANIFEST file

* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-7mdk
- rebuild for new Perl

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.15-6mdk
- rebuild for new perl
- rm -rf /home/guillomovitch/rpm/tmp/perl-Error-0.17001 in %%install, not %%prep
- drop Prefix tag
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

