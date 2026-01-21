# mapreduce2025
MapReduce samples and exercises

## Obxectivo
- Comprender o funcionamento do traballo distribuído baseado en técnicas MapReduce.
- Modificar mappers e reducer para obter diferentes resultados a partir dos datos.

## Arquivos principais do repositorio

```./README.md``` : este arquivo.

```./exercises/``` : este cartafol contén<br>
- Os cartafoles fillos de exercicios
```
./exercises/exercise1/
(...)
./exercises/exercise6/
```
Estes conteñen cadanseu arquivo ```mapper.py``` e ```reducer.py```.

- O cartafol fillo de arquivos de entrada
```./exercises/files```
Contén os arquivos de entrada de datos (```salesdata.txt```), e os de probas e control de integridade da entrada de datos (```testsales.txt``` e ```bad_data.txt```).

<br>

```./generator```: cartafol que contén  ```sales_generator.py``` para xerar o arquivo de entrada de datos  (o devandito ```salesdata.txt```)

```./sample``` : cartafol que contén os arquivos de mostra ```mapper.py```, ```reducer.py``` e ```testsales.txt```.


## Restriccións e caveats da execución 

Estes exercicios desenroláronse no Cluster Hadoop do Centro de Supercomputación de Galicia (CESGA). 
[Ligazón dos servizos Big Data do CESGA](https://bigdata.cesga.es/).

Caveats:
- Os scripts deberán ser compatíbeis con Python 2.7 .
- Os arquivos de entrada deberán estar no Cluster de Hadoop (HDFS). 

## Como acarrexar (subir) arquivos

- Do equipo terminal de traballo (PC, portátil...) ó Nodo Pasarela (*Gateway Node*)

```scp <arquivo_local> hadoop:```

- Do Nodo Pasarela ó cluster Hadoop (HDFS).
```hdfs dfs -put <arquivo>```

<br>
Do mesmo xeito, poderiamos descarrexar arquivos de xeito inverso cos comandos:

```hdfs dfs -get <arquivo>```

```scp hadoop:<arquivo> .```

**NOTA**: A conexión precisa ter instalados os certificados no terminal de traballo (no cartafol ```~/.ssh/id_rsa```).
Asimesmo, se o host hadoop (que é o Nodo Pasarela) non está engadido a ```.ssh/config``` haberá que: ou ben engadilo, ou ben trocar ```hadoop``` por ```hadoop.cesga.es```.

Para engadilo a ```.ssh/config```

```
Host hadoop
        Hostname hadoop.cesga.es
        User <o_teu_usuario>
        IdentityFile ~/.ssh/id_rsa
```
## Emprego dos arquivos de exercicios

Para arrebolar (executar) cómpre empregar comandos tales como:
```
mapred streaming \
  -files mapper.py,reducer.py,testsales.txt \
  -input /data/salesdata.txt \
  -output <CARTAFOL_DE_SAIDA> \
  -mapper "python mapper.py" \
  -reducer "python reducer.py"
```

Podemos copiar a saída de MapReduce a un ficheiro empregando a redirección estándar
```
hdfs dfs -cat <CARTAFOL_DE_SAIDA>/* > arquivo_saida.txt
```

**NOTAS**: 
- Os exercicios 4 e 5 non devolven un valor senón todos por mor da paralelización dos traballos de MapReduce. Para obter unha soa saída temos dúas solucións (*workarounds*) posibles:
1. Engadir ```-D mapreduce.job.reduces=1``` ó comando ```mapreduce```.
2. Pasar a saída de MapReduce por reducer.py en local:
```
cat max_tipo_pago.txt | python reducer.py
```
<br>

- O arquivo ```testsales.txt``` emprégase en ```mapper.py``` para almacenar os valores posibles de tendas, artigos, etc. para cotexar os datos propios de entrada.
<br>

## Automatización da execución
No cartafol ```./exercises/exercise1``` engadíronse 2 exemplos de automatización:<br>
- ```launcher1.py```: automatiza a execución principal (```mapred```)<br>
- ```gather.py``` automatiza a obtención do arquivo de texto cos resultados de MapReduce.

## 以上



