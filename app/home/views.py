from django.shortcuts import render
from reserva.models import *
from django.views.generic.list import View
from backend.models import AuthUser
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class index(View):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("select count(*) as count_equip from reserva where tipo_reserva = 'E' and substring(data_inicio,6,2) = substring(now(),6,2)")
        equip = dictfetchall(cursor)

        cursor.execute("select count(*) as count_sala from reserva where tipo_reserva = 'S' and substring(data_inicio,6,2) = substring(now(),6,2)")
        sala = dictfetchall(cursor)

        cursor.execute("select count(*) as count_veiculo from reserva where tipo_reserva = 'V' and substring(data_inicio,6,2) = substring(now(),6,2)")
        veiculo = dictfetchall(cursor)

        cursor.execute("select count(*) as count_multiplo from reserva where tipo_reserva = 'M' and substring(data_inicio,6,2) = substring(now(),6,2)")
        multiplo = dictfetchall(cursor)

        cursor.execute(""" select auth_user.first_name as nome,
                                 auth_user.username as usuario,                                 
                                 reserva.data_inicio,
                                 reserva.data_final,
                                 horario.descricao as horario,
                                 case 
                                    when reserva.id_equipamento is not null then equipamento.descricao
                                    when reserva.id_sala is not null then sala.descricao 
                                    when reserva.id_veiculo is not null then  veiculo.modelo
                                else '' end descricao_tipo_reserva,     
                                 reserva.observacoes,
                                 reserva.tipo_reserva
                                 from reserva
                                    left join auth_user on auth_user.id = reserva.id_usuario
                                    left join horario on horario.id = reserva.id_horario
                                    left join equipamento on equipamento.id = reserva.id_equipamento
                                    left join sala on sala.id = reserva.id_sala
                                    left join veiculo on veiculo.id = reserva.id_veiculo""")
        reservas = dictfetchall(cursor)

        lista = {}
        lista['equip'] = equip
        lista['sala'] = sala
        lista['veiculo'] = veiculo
        lista['multiplo'] = multiplo
        lista['reservas'] = reservas


        return render(request, 'index.html',  lista)
