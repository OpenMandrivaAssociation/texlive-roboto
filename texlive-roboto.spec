%global tl_name roboto
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Roboto family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/roboto
License:	apache2 ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roboto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roboto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Roboto Sans, Roboto Condensed, Roboto Mono, Roboto Slab and Roboto
Serif families of fonts, designed by Christian Robertson and Greg
Gazdowicz for Google.

