%define 	modulename pam_radius
Summary:	PAM module - authenticate using RADIUS server
Summary(pl):	Modu³ PAM pozwalaj±cy na u¿ycie serwera RADIUS do uwierzytelniania
Name:		pam-%{modulename}_auth
Version:	1.3.16
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://ftp.freeradius.org/pub/radius/%{modulename}-%{version}.tar
# Source0-md5:	633d57c7035671fe7655158e37633db7
URL:		http://www.freeradius.org/pam_radius_auth/
BuildRequires:	pam-static > 0.77.3-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%description -l pl
To jest modu³ do PAM s³u¿±cy uwierzytelnianiu u¿ytkowników w RADIUSie.
Pozwala ka¿dej maszynie korzystaj±cej z PAMa zostaæ klientem RADIUSa w
celach uwierzytelniania u¿ytkowników oraz zbierania statystyk logowañ
(accounting). Niezbêdny do niego jest serwer RADIUS ¿eby móc dokonaæ
samego uwierzytelnienia.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/security

install pam_radius_auth.so $RPM_BUILD_ROOT/lib/security

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO USAGE INSTALL pam_radius_auth.conf
%attr(755,root,root) /lib/security/pam_radius_auth.so
