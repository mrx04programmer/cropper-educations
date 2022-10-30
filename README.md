# Cropper-Pentester-Tool para uso Institucional

<!-- Logo -->
<div align="center">
    <img src="https://user-images.githubusercontent.com/46001898/198858484-182e4f02-5345-4646-b5ba-253aa645ff79.png" width="30%" style="border-radius: 30px;"><br><br><img src="https://img.shields.io/badge/status-stable-t?style=for-the-badge&color=darkgreen&logoColor=darkgreen&labelColor=black">
</div>



<div align="center">
<h3>¿Comó surgió?</h3>
Monitorear una red local por medio de envenenamiento puede llamar mucho la atención, para ello se llevo a cabo un silencioso monitoreo teniendo en cuenta las reglas ARP, con base a esto se crea el Proyecto de Cropper.
</div>
<br>


<h3>¿Comó funciona?</h3>

> Primero hay que entender como llega un paquete de red a un router o modem:
El paquete de red es enviado al corta fuegos del router y de allí se verifica si es una petición de router o externa.
<div align="center">
<img  src="https://user-images.githubusercontent.com/46001898/198860316-83a94d5e-15d4-4614-b8d2-ce1edea06eb8.png" width="50%">
</div>

> Sabiendo lo anterior, se procede a inyectar un payload en un paquete de red de estado normal y el cual sabemos que será aceptado en el corta fuegos.

>Las peticiones que el cortafuego aceptará como petición de router son:

| Nombre de Petición | Protocolo|
|--------------------|----------|
| gateway whois      | TCP      |
| gateway redirect   | UDP      |
| gateway login      | TCP      |

> Para realizar la correspondiente inyección a un paquete de este tipo de petición , se utiliza de intermediario Cropper para que el router reciba el paquete como propio.
<div align="center">
<img src="https://user-images.githubusercontent.com/46001898/198860812-f113974b-6bc6-4ed3-bf90-cbc68b7ef9dd.png" width="50%">
</div>

<h3>Estadísticas <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.iconpacks.net%2Ficons%2F1%2Ffree-pie-chart-icon-683-thumb.png&f=1&nofb=1&ipt=697a80c1a06d2203239587d7dac980bc80ae0f95bf3289f64160c32c28a6b52e&ipo=images" width="25px"></h3>
<div>
    <div style="width: 2000px">
        <p> Tras la evolución de herramientas de pentesting , se han realizado variedades de ataques para poder observar y manipular el trafico de una red. Entre estos ataques encontramos MITM, ProxySpoofing y Envenenamiento de reglas ARP.
        El porcentaje de escandalo generado por envenenamiento es del 75% (esto teniendo en cuenta que existen varias herramientas que utilizan diferentes formas para un mismo ataque) y un ataque sin envenenamiento es colado en la red y es detectado en un 15%.</p>
    <div>
</div>
