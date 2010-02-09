Summary:	Free UCS fonts for ancient Aegean scripts
Summary(pl.UTF-8):	Wolnodostępne fonty UCS dla starożytnych pism basenu Morza Egejskiego
Name:		fonts-OTF-Aegean
Version:	3.01
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://users.teilar.gr/~g1951d/Aegean.zip
# Source0-md5:	36201de0f8a523a3c002bb8619fc9da9
Source1:	http://users.teilar.gr/~g1951d/Anatolian.zip
# Source1-md5:	857dd55cdb7b8ba54b69023f05e92114
URL:		http://users.teilar.gr/~g1951d/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
Aegean font covers the following scripts and symbols supported by The
Unicode Standard 5.2: Basic Latin, Greek and Coptic, Greek Extended,
some Punctuation and other Symbols, Linear B Syllabary, Linear B
Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols,
Phaistos Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian,
Cypriot Syllabary, Phoenician, Lydian, and Archaic Greek Musical
Notation. Aegean allocates in the Supplementary Private Use Plane 15,
the following scripts and symbols, as yet unsupported by Unicode:
Cretan Hieroglyphs, Cypro-Minoan, Linear A, the Arkalochori Axe,
Ancient Greek and Old Italic variant alphabets.

Anatolian Hieroglyphs are available in the work-font, Anatolian. 

%%description -l pl.UTF-8
#TODO

%prep
%setup -q -c -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install *.otf $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{otffontsdir}/Aegean.otf
%{otffontsdir}/Anatolian.otf
