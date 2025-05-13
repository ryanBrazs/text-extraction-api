package com.pi.pi_ods3.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.pi.pi_ods3.models.Medicamento;
import com.pi.pi_ods3.service.MedicamentoService;

@RestController
@RequestMapping("/api/medicamentos")
public class MedicamentoController {
    @Autowired
    private MedicamentoService service;

    @GetMapping
    public List<Medicamento> listarTodos() {
        return service.listarTodos();
    }

    @GetMapping("/buscar/{nome}")
    public List<Medicamento> buscarPorNome(@PathVariable String nome) {
        return service.buscarPorNome(nome);
    }

}
