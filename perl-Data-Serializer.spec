#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Serializer
Version  : 0.60
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-0.60.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEELY/Data-Serializer-0.60.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-serializer-perl/libdata-serializer-perl_0.60-2.debian.tar.xz
Summary  : Modules that serialize data structures
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Serializer-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl-Module-Build

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

%description dev
dev components for the perl-Data-Serializer package.


%package license
Summary: license components for the perl-Data-Serializer package.
Group: Default

%description license
license components for the perl-Data-Serializer package.


%prep
%setup -q -n Data-Serializer-0.60
cd ..
%setup -q -T -D -n Data-Serializer-0.60 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-Serializer-0.60/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Serializer
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Serializer/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Bencode.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Config/General.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Convert/Bencode.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Convert/Bencode_XS.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Cookbook.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Data/Denter.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Data/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Data/Taxi.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/FreezeThaw.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/JSON/Syck.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/PHP/Serialization.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Persistent.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Raw.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/Storable.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/XML/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/XML/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/YAML.pm
/usr/lib/perl5/vendor_perl/5.28.1/Data/Serializer/YAML/Syck.pm

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
/usr/share/package-licenses/perl-Data-Serializer/deblicense_copyright
