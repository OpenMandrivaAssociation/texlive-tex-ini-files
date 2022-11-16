Name:		texlive-tex-ini-files
Version:	40533
Release:	1
Summary:	Model TeX format creation files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tex-ini-files
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides a collection of model .ini files for
creating TeX formats. These files are commonly used to
introduced distribution-dependent variations in formats. They
are also used to allow existing format source files to be used
with newer engines, for example to adapt the plain e-TeX source
file to work with XeTeX and LuaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/tex-ini-files
%doc %{_texmfdistdir}/doc/generic/tex-ini-files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
