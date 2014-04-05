<?php

# Connection to a running namecoin node
$jsonConnect = 'http://username:password@127.0.0.1:8336/';

# DNS server names which are authoritative for the .bit zone (the DNS servers you are building/configuring)
$authoritativeNS[] = array('hostname', array('1.2.3.4', '1.2.3.5', '2001:5::1'));

# Use another template file
#$templateFile = dirname(__FILE__).'/zone-template-second.conf';

# Allowed namespaces
$zonesNamespace = array( 'd/' => 'bit', );

# Cache data to avoid generating zones each time
$cacheDir = dirname(__FILE__).'/cache/';

# Bind configuration files for the .bit zone
$bindZonesList = '/etc/bind/dotbit/';

# Bind zones for .bit domains
$bindZonesFiles= '/etc/bind/dotbit/zones/';

# Namecoin stat folder, leave empty to disable
#$statDir = dirname(__FILE__).'/stats/';

# Debug
$doFileWrites = true;
#$showErrors = true;

?>
