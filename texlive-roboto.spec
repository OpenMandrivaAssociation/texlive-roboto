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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Roboto Sans, Roboto Condensed, Roboto Mono, Roboto Slab and Roboto
Serif families of fonts, designed by Christian Robertson and Greg
Gazdowicz for Google.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from roboto:
Map roboto.map
TL_DROPIN_EOF
