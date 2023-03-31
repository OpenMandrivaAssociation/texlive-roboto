Name:		texlive-roboto
Version:	64350
Release:	2
Summary:	Support for the Roboto family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/roboto
License:	apache2 ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roboto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roboto.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Roboto Sans, Roboto Condensed, Roboto Mono,
Roboto Slab and Roboto Serif families of fonts, designed by
Christian Robertson and Greg Gazdowicz for Google.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/roboto
%{_texmfdistdir}/fonts/vf/google/roboto
%{_texmfdistdir}/fonts/type1/google/roboto
%{_texmfdistdir}/fonts/tfm/google/roboto
%{_texmfdistdir}/fonts/opentype/google/roboto
%{_texmfdistdir}/fonts/map/dvips/roboto
%{_texmfdistdir}/fonts/enc/dvips/roboto
%doc %{_texmfdistdir}/doc/fonts/roboto

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
