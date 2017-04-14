#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	ErrorHandler
Summary:	Class::ErrorHandler - base class for error handling
Summary(pl.UTF-8):	Class::ErrorHandler - klasa bazowa do obsługi błędów
Name:		perl-Class-ErrorHandler
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8b525e84384752b7cabc7d7f1ed0c823
URL:		http://search.cpan.org/dist/Class-ErrorHandler/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Class::ErrorHandler, a base class for classes that need to do
error handling (which is, probably, most of them).

%description -l pl.UTF-8
To jest Class::ErrorHandler - klasa bazowa dla klas potrzebujących
obsługiwać błędy (czyli prawdopodobnie większości).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/Class/ErrorHandler.pm
%{_mandir}/man3/*
