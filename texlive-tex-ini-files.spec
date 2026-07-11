%global tl_name tex-ini-files
%global tl_revision 78524

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Model TeX format creation files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/tex-ini-files
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ini-files.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a collection of model .ini files for creating TeX
formats. These files are commonly used to introduce distribution-
dependent variations in formats. They are also used to allow existing
format source files to be used with newer engines, for example to adapt
the plain e-TeX source file to work with XeTeX and LuaTeX.

