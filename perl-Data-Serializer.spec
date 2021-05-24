#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Serializer
Version  : 0.65
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-0.65.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-0.65.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-serializer-perl/libdata-serializer-perl_0.60-2.debian.tar.xz
Summary  : Modules that serialize data structures
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Serializer-license = %{version}-%{release}
Requires: perl-Data-Serializer-perl = %{version}-%{release}
Requires: perl(Bencode)
Requires: perl(Convert::Bencode)
Requires: perl(Convert::Bencode_XS)
Requires: perl(Data::Denter)
Requires: perl(Data::Taxi)
Requires: perl(PHP::Serialization)
Requires: perl(XML::Dumper)
BuildRequires : buildreq-cpan

%description
NAME
Data::Serializer:: - Modules that serialize data structures
SYNOPSIS
use Data::Serializer;

$obj = Data::Serializer->new();

%package dev
Summary: dev components for the perl-Data-Serializer package.
Group: Development
Provides: perl-Data-Serializer-devel = %{version}-%{release}
Requires: perl-Data-Serializer = %{version}-%{release}

%description dev
dev components for the perl-Data-Serializer package.


%package license
Summary: license components for the perl-Data-Serializer package.
Group: Default

%description license
license components for the perl-Data-Serializer package.


%package perl
Summary: perl components for the perl-Data-Serializer package.
Group: Default
Requires: perl-Data-Serializer = %{version}-%{release}

%description perl
perl components for the perl-Data-Serializer package.


%prep
%setup -q -n Data-Serializer-0.65
cd %{_builddir}
tar xf %{_sourcedir}/libdata-serializer-perl_0.60-2.debian.tar.xz
cd %{_builddir}/Data-Serializer-0.65
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Serializer-0.65/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Serializer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Serializer/7f76ad22b4b668eaf9159ac6396a33fd70180bfd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Serializer.3
/usr/share/man/man3/Data::Serializer::Bencode.3
/usr/share/man/man3/Data::Serializer::Config::General.3
/usr/share/man/man3/Data::Serializer::Convert::Bencode.3
/usr/share/man/man3/Data::Serializer::Convert::Bencode_XS.3
/usr/share/man/man3/Data::Serializer::Cookbook.3
/usr/share/man/man3/Data::Serializer::Data::Denter.3
/usr/share/man/man3/Data::Serializer::Data::Dumper.3
/usr/share/man/man3/Data::Serializer::Data::Taxi.3
/usr/share/man/man3/Data::Serializer::FreezeThaw.3
/usr/share/man/man3/Data::Serializer::JSON.3
/usr/share/man/man3/Data::Serializer::JSON::Syck.3
/usr/share/man/man3/Data::Serializer::PHP::Serialization.3
/usr/share/man/man3/Data::Serializer::Persistent.3
/usr/share/man/man3/Data::Serializer::Raw.3
/usr/share/man/man3/Data::Serializer::Storable.3
/usr/share/man/man3/Data::Serializer::XML::Dumper.3
/usr/share/man/man3/Data::Serializer::XML::Simple.3
/usr/share/man/man3/Data::Serializer::YAML.3
/usr/share/man/man3/Data::Serializer::YAML::Syck.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Serializer/7f76ad22b4b668eaf9159ac6396a33fd70180bfd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Bencode.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Config/General.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Convert/Bencode.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Convert/Bencode_XS.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Cookbook.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Data/Denter.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Data/Dumper.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Data/Taxi.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/FreezeThaw.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/JSON.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/JSON/Syck.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/PHP/Serialization.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Persistent.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Raw.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/Storable.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/XML/Dumper.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/XML/Simple.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/YAML.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Serializer/YAML/Syck.pm
